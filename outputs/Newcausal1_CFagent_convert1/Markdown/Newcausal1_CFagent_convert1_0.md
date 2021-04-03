
# Parameters

    Name :                      Newcausal1_CFagent_convert1-0
    Main :                      CFagent
    Level :                     Levels.Causal1
    Hours :                     3.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        500000.0
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        100000.0
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoors :            True
    Layer redkeys :             True
    Layer bluedoors :           True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                0
    Minutes used :              175 minutes.
    Hours used :                2 hours.

# Profiling


      5892478480 function calls (5848133281 primitive calls) in 10509.99 seconds

##    Ordered by: cumulative time
   List reduced from 485 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 10509.993 10509.993 {built-in method builtins.exec}
                      1    4.706    4.706 10509.993 10509.993 <string>:1(<module>)
                      1   40.256   40.256 10505.287 10505.287 main.py:96(CFagent)
                1351932    5.535    0.000 3470.913    0.003 agent.py:28(learn)
                1351930   90.826    0.000 2800.925    0.002 learner.py:42(Qlearn)
        49540945/5197437  213.181    0.000 1684.045    0.000 module.py:866(_call_impl)
                 450644    2.593    0.000 1672.574    0.004 game.py:36(step)
                 450644    3.176    0.000 1580.556    0.004 layers.py:594(step)
                3845507   10.552    0.000 1574.238    0.000 network.py:24(forward)
                3845507   50.470    0.000 1536.254    0.000 container.py:117(forward)
                 450644   57.283    0.000 1355.770    0.003 agent.py:53(_learn)
                 450644  190.010    0.000 1283.418    0.003 agent.py:197(counterfact)
                 450644   55.807    0.000 1238.616    0.003 agent.py:189(_learn)
                1351930   12.633    0.000 1070.516    0.001 optimizer.py:84(wrapper)
                1351930    6.559    0.000 1017.490    0.001 grad_mode.py:24(decorate_context)
                1351930   44.555    0.000  996.687    0.001 adam.py:55(step)
                 450644  580.680    0.001  975.701    0.002 replaybuffer.py:28(teleporter_save_data)
                1351930  209.432    0.000  903.250    0.001 _functional.py:53(adam)
                 450644   14.605    0.000  867.005    0.002 agent.py:114(_learn)
                 450644  660.451    0.001  846.289    0.002 replaybuffer.py:22(sample_data)
                1246651   37.535    0.000  840.356    0.001 agent.py:48(__call__)
                 450644   43.648    0.000  793.717    0.002 layers.py:18(step)
                 450645   54.776    0.000  778.505    0.002 layers.py:565(update)
               44896927   57.491    0.000  745.891    0.000 layer.py:82(move)
                1351930    6.216    0.000  745.543    0.001 tensor.py:195(backward)
                1351930    6.056    0.000  739.101    0.001 __init__.py:68(backward)
                 450644  411.370    0.001  708.204    0.002 agent.py:85(interveen)
                1351930  704.314    0.001  704.314    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 450644  508.993    0.001  675.591    0.001 replaybuffer.py:49(sample_data)
                7691014   18.589    0.000  563.199    0.000 conv.py:398(forward)
                7691014   11.695    0.000  535.727    0.000 conv.py:390(_conv_forward)
                7691014  524.033    0.000  524.033    0.000 {built-in method conv2d}
                 345640    3.793    0.000  461.239    0.001 agent.py:167(choose_action)
                6074528  455.855    0.000  455.855    0.000 {built-in method tensor}
               10635233   22.653    0.000  434.685    0.000 linear.py:93(forward)
                5048544    3.915    0.000  430.368    0.000 game.py:32(board)
                5407734  245.430    0.000  425.710    0.000 layer.py:143(NoRock_update)
               10635233    9.378    0.000  400.264    0.000 functional.py:1737(linear)
               39987805  392.159    0.000  392.159    0.000 {built-in method clone}
               10635233  388.693    0.000  388.693    0.000 {built-in method torch._C._nn.linear}
                1097755   10.322    0.000  348.474    0.000 layers.py:615(restart)
               44893427   54.228    0.000  325.673    0.000 layers.py:605(isFree)
                 450644  199.052    0.000  323.476    0.001 agent.py:66(modify)
               44896927   76.848    0.000  306.503    0.000 layers.py:611(check)
                6654369  287.279    0.000  287.279    0.000 {built-in method cat}
              244139634  232.713    0.000  271.444    0.000 layer.py:79(isFree)
                1097755    5.308    0.000  257.292    0.000 level.py:8(__init__)
               14480740   12.666    0.000  230.276    0.000 activation.py:713(forward)
                1697295   11.859    0.000  230.067    0.000 agent.py:58(modify_board)
               14480740   12.720    0.000  217.610    0.000 functional.py:1364(leaky_relu)
                1097755   13.639    0.000  217.545    0.000 levels.py:122(generate)
                 450642    9.686    0.000  214.742    0.000 agent.py:163(__call__)
               14480740  202.423    0.000  202.423    0.000 {built-in method torch._C._nn.leaky_relu}
                 450644  100.775    0.000  198.767    0.000 replaybuffer.py:55(CF_save_data)
                 450644    9.189    0.000  198.475    0.000 agent.py:109(__call__)
                4281246   37.344    0.000  191.687    0.000 level.py:41(notUsed)
               25236024  175.633    0.000  175.633    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1351930   28.694    0.000  156.299    0.000 optimizer.py:189(zero_grad)
               25236024  155.309    0.000  155.309    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                1697295  152.500    0.000  152.500    0.000 {built-in method torch._C._nn.one_hot}
                 450644   16.628    0.000  149.390    0.000 replaybuffer.py:18(stacker)
               45064500   13.912    0.000  132.388    0.000 {built-in method builtins.all}
                 450642   16.599    0.000  131.870    0.000 replaybuffer.py:45(stacker)
              142636416   36.814    0.000  123.892    0.000 layers.py:571(<genexpr>)
              172861030  106.830    0.000  106.830    0.000 layer.py:122(elements)
               12618012  104.075    0.000  104.075    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              378777312   69.396    0.000  101.441    0.000 enum.py:646(__hash__)
               12618012   90.949    0.000   90.949    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               44896927   56.656    0.000   88.111    0.000 layers.py:143(check)
                1246651   30.549    0.000   84.904    0.000 exploration.py:53(softmaxer)
               42135742   84.504    0.000   84.504    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               12618012   82.255    0.000   82.255    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               12618012   82.137    0.000   82.137    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               45064500   56.673    0.000   81.598    0.000 layers.py:111(isDone)
                 345640   63.662    0.000   78.450    0.000 agent.py:178(convert_values)
                6586530    6.987    0.000   78.430    0.000 layer.py:56(restart)
                4281246    3.430    0.000   75.898    0.000 level.py:38(elementsIn)
               88326168   61.346    0.000   75.741    0.000 tensor.py:906(grad)
                 450644   41.719    0.000   70.452    0.000 collector.py:54(collect)
                 901288   26.629    0.000   69.561    0.000 random.py:315(sample)
               44896927   45.681    0.000   66.651    0.000 layers.py:47(check)
                1351930    2.510    0.000   64.693    0.000 loss.py:527(forward)
        765929691/765929688   55.607    0.000   64.610    0.000 {built-in method builtins.len}
               44896927   41.454    0.000   63.304    0.000 layers.py:124(check)
                1351930    6.022    0.000   62.183    0.000 functional.py:2898(mse_loss)
               12618012   60.382    0.000   60.382    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                1351933   58.909    0.000   58.909    0.000 {built-in method nonzero}
                1097855   29.113    0.000   58.700    0.000 layers.py:33(reset)
              197478799   55.766    0.000   55.766    0.000 level.py:32(inverse)
               81469845   34.867    0.000   47.522    0.000 layer.py:106(add)
              507862617   47.488    0.000   47.488    0.000 layer.py:75(positions)
                4281246   23.747    0.000   47.225    0.000 level.py:39(<listcomp>)
               40294182   29.646    0.000   40.943    0.000 layer.py:102(remove)
                1351930   37.927    0.000   37.927    0.000 {built-in method torch._C._nn.mse_loss}
                7691014    5.884    0.000   37.700    0.000 flatten.py:39(forward)
                1352099   34.022    0.000   34.022    0.000 {built-in method max}
                2148214    3.305    0.000   33.343    0.000 tensor.py:525(__rsub__)
               49367323   22.220    0.000   32.948    0.000 random.py:250(_randbelow_with_getrandbits)
              378783055   32.047    0.000   32.047    0.000 {built-in method builtins.hash}
                7691014   31.817    0.000   31.817    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 9493844: <Newcausal1_CFagent_convert1_0> in cluster <dcc> Done

Job <Newcausal1_CFagent_convert1_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Apr  3 15:09:50 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Apr  3 15:09:51 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr  3 15:09:51 2021
Terminated at Sat Apr  3 18:05:06 2021
Results reported at Sat Apr  3 18:05:06 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   10485.08 sec.
    Max Memory :                                 4370 MB
    Average Memory :                             3906.42 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12014.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   10619 sec.
    Turnaround time :                            10516 sec.

The output (if any) is above this job summary.

