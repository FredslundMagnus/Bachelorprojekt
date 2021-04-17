
# Parameters

    Name :                      causal7_demo-0
    Main :                      teleport
    Level :                     Levels.Causal7
    Hours :                     16.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
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
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Counterfacts :              10
    Topn :                      7
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      41205442422 function calls (41052769331 primitive calls) in 57307.09 seconds

##    Ordered by: cumulative time
   List reduced from 474 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57307.089 57307.089 {built-in method builtins.exec}
                      1    1.799    1.799 57307.089 57307.089 <string>:1(<module>)
                      1  129.183  129.183 57305.290 57305.290 main.py:40(teleport)
                5452990   20.056    0.000 19589.865    0.004 agent.py:29(learn)
                5452990  460.305    0.000 16804.560    0.003 learner.py:42(Qlearn)
                2726495   95.806    0.000 11756.676    0.004 agent.py:54(_learn)
                2726495   11.738    0.000 11358.736    0.004 game.py:41(step)
                2726495   13.787    0.000 10730.363    0.004 layers.py:710(step)
                2726495 5405.091    0.002 10459.048    0.004 replaybuffer.py:28(teleporter_save_data)
                2726495   80.478    0.000 7800.004    0.003 agent.py:117(_learn)
        171756575/19084495  698.658    0.000 7581.799    0.000 module.py:715(_call_impl)
                5452990   33.806    0.000 7166.398    0.001 grad_mode.py:23(decorate_context)
               13631505   35.241    0.000 7104.445    0.001 network.py:24(forward)
                5452990  183.471    0.000 7068.145    0.001 adam.py:55(step)
               13631505  180.816    0.000 6986.931    0.001 container.py:115(forward)
                2726495 4427.919    0.002 6734.549    0.002 agent.py:88(interveen)
                5452990 1287.068    0.000 6075.981    0.001 functional.py:53(adam)
                2726495  229.608    0.000 5924.080    0.002 layers.py:17(step)
              272649500  462.831    0.000 5667.011    0.000 layer.py:98(move)
                2726496  389.273    0.000 4774.280    0.002 layers.py:676(update)
                5452020  128.744    0.000 4635.913    0.001 agent.py:49(__call__)
              276950158 3933.534    0.000 3933.534    0.000 {built-in method clone}
                5452990   40.049    0.000 3889.629    0.001 tensor.py:181(backward)
                5452990   19.489    0.000 3849.579    0.001 __init__.py:68(backward)
                5452990 3684.298    0.001 3684.298    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2726495 2102.671    0.001 3541.345    0.001 replaybuffer.py:22(sample_data)
              272649500  550.885    0.000 3199.433    0.000 layers.py:727(check)
                2726495 1613.142    0.001 3051.476    0.001 agent.py:67(modify)
               27263010   48.255    0.000 2525.106    0.000 conv.py:422(forward)
               27263010   52.269    0.000 2454.785    0.000 conv.py:414(_conv_forward)
               27263010 2392.578    0.000 2392.578    0.000 {built-in method conv2d}
               35441525   83.082    0.000 2272.819    0.000 linear.py:92(forward)
               35441525  142.344    0.000 2152.993    0.000 functional.py:1669(linear)
              272649500  408.853    0.000 1576.435    0.000 layers.py:721(isFree)
               35441525 1534.325    0.000 1534.325    0.000 {built-in method addmm}
              343538424  955.068    0.000 1511.113    0.000 tensor.py:933(grad)
               24537485 1495.595    0.000 1495.595    0.000 {built-in method cat}
                2726495   37.344    0.000 1464.872    0.001 agent.py:112(__call__)
                3656626   31.980    0.000 1462.033    0.000 layers.py:731(restart)
                5452990  137.166    0.000 1453.914    0.000 optimizer.py:167(zero_grad)
              762483937  402.693    0.000 1379.570    0.000 {built-in method builtins.any}
                8178515   58.243    0.000 1365.107    0.000 agent.py:59(modify_board)
               19085472  720.173    0.000 1270.779    0.000 layer.py:167(NoRock_update)
               98153820 1259.746    0.000 1259.746    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2726495   53.126    0.000 1241.774    0.000 replaybuffer.py:18(stacker)
              285128673 1203.789    0.000 1203.789    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                3656626   16.537    0.000 1171.105    0.000 level.py:8(__init__)
             1886855540  925.995    0.000 1167.582    0.000 layer.py:95(isFree)
               98153820 1068.739    0.000 1068.739    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             4119237035  720.920    0.000 1060.331    0.000 enum.py:646(__hash__)
               49073030   43.931    0.000 1046.360    0.000 activation.py:713(forward)
               49073030   68.990    0.000 1002.429    0.000 functional.py:1292(leaky_relu)
                3656626   43.559    0.000  995.942    0.000 levels.py:446(generate)
               49073030  926.850    0.000  926.850    0.000 {built-in method torch._C._nn.leaky_relu}
               17550727  169.686    0.000  906.870    0.000 level.py:41(notUsed)
               11780634  860.146    0.000  860.146    0.000 {built-in method tensor}
                8178515  849.427    0.000  849.427    0.000 {built-in method torch._C._nn.one_hot}
              272649500  474.245    0.000  776.185    0.000 layers.py:610(check)
              447143457  254.994    0.000  747.234    0.000 overrides.py:1070(has_torch_function)
               19087053  105.541    0.000  744.626    0.000 tensor.py:21(wrapped)
              272649500  438.949    0.000  734.457    0.000 layers.py:595(check)
              272649500  441.714    0.000  727.565    0.000 layers.py:625(check)
               49076910  724.619    0.000  724.619    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             2151943792  559.792    0.000  692.101    0.000 layers.py:692(<genexpr>)
                2726495  398.442    0.000  670.631    0.000 collector.py:53(collect)
              291736653   79.448    0.000  655.996    0.000 {built-in method builtins.all}
                5452990    6.550    0.000  637.367    0.000 game.py:37(board)
               49076910  633.054    0.000  633.054    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              568679364  131.194    0.000  598.984    0.000 layers.py:682(<genexpr>)
               49076910  570.891    0.000  570.891    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               49076910  515.032    0.000  515.032    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                5452020  174.592    0.000  492.235    0.000 exploration.py:53(softmaxer)
             4639079826  460.720    0.000  460.720    0.000 layer.py:91(positions)
              272649600  298.806    0.000  460.211    0.000 layers.py:107(isDone)
               17550727   13.665    0.000  420.955    0.000 level.py:38(elementsIn)
               49076910  403.095    0.000  403.095    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             4119257018  339.415    0.000  339.415    0.000 {built-in method builtins.hash}
              272649500  213.922    0.000  334.565    0.000 layers.py:581(check)
              827289824  323.910    0.000  323.910    0.000 layer.py:146(elements)
                5452990    7.443    0.000  316.814    0.000 loss.py:445(forward)
               13632475  311.488    0.000  311.488    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                5452990   28.873    0.000  309.372    0.000 functional.py:2637(mse_loss)
               35441525  308.900    0.000  308.900    0.000 {method 't' of 'torch._C._TensorBase' objects}
              948814947  222.710    0.000  281.024    0.000 overrides.py:1083(<genexpr>)
               17550727  129.687    0.000  273.068    0.000 level.py:39(<listcomp>)
        2340104339/2340104337  186.863    0.000  269.983    0.000 {built-in method builtins.len}
               16358970  268.448    0.000  268.448    0.000 {built-in method sum}
               25596382   22.069    0.000  249.846    0.000 layer.py:69(restart)
              396369979  163.071    0.000  225.638    0.000 layer.py:130(add)
              271570098  132.287    0.000  196.190    0.000 layer.py:126(remove)
                5452990  195.905    0.000  195.905    0.000 {built-in method torch._C._nn.mse_loss}
             1886855540  193.697    0.000  193.697    0.000 layer.py:203(isBlocking)
               27263010   18.836    0.000  192.187    0.000 flatten.py:39(forward)
                2726495   71.471    0.000  191.758    0.000 random.py:315(sample)
                3656726   94.950    0.000  191.325    0.000 layers.py:30(reset)
              842655750  187.677    0.000  187.677    0.000 level.py:32(inverse)
                2727585  176.298    0.000  176.298    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
                5453807  175.731    0.000  175.731    0.000 {built-in method max}
               27263010  173.351    0.000  173.351    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                5452020  161.057    0.000  161.057    0.000 {built-in method multinomial}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-13>
Subject: Job 9501880: <causal7_demo_0> in cluster <dcc> Done

Job <causal7_demo_0> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Wed Apr  7 15:59:17 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Apr  7 20:55:52 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr  7 20:55:52 2021
Terminated at Thu Apr  8 12:51:02 2021
Results reported at Thu Apr  8 12:51:02 2021

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

    CPU time :                                   57244.93 sec.
    Max Memory :                                 2816 MB
    Average Memory :                             2812.05 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13568.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57326 sec.
    Turnaround time :                            75105 sec.

The output (if any) is above this job summary.

