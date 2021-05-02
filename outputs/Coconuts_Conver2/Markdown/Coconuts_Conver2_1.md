
# Parameters

    Name :                      Coconuts_Conver2-1
    Main :                      CFagent
    Level :                     Levels.Coconuts
    Failed actions chance :     0.0
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
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
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      73583760575 function calls (73222282388 primitive calls) in 86108.85 seconds

##    Ordered by: cumulative time
   List reduced from 511 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86108.851 86108.851 {built-in method builtins.exec}
                      1    4.104    4.104 86108.851 86108.851 <string>:1(<module>)
                      1  368.110  368.110 86104.747 86104.747 main.py:79(CFagent)
               12216921   49.113    0.000 29465.809    0.002 agent.py:29(learn)
               12216921  729.336    0.000 24184.162    0.002 learner.py:42(Qlearn)
                4072307   16.959    0.000 22235.699    0.005 game.py:41(step)
                4072307   21.983    0.000 21432.878    0.005 layers.py:718(step)
                4072307  376.950    0.000 14898.634    0.004 layers.py:17(step)
              407046869 1513.943    0.000 14483.258    0.000 layer.py:98(move)
        405173894/43697398 1607.560    0.000 12887.393    0.000 module.py:866(_call_impl)
               31480477   85.510    0.000 12018.645    0.000 network.py:27(forward)
               31480477  400.578    0.000 11734.735    0.000 container.py:117(forward)
                4072307  372.787    0.000 11409.837    0.003 agent.py:54(_learn)
                4072307  367.497    0.000 10490.455    0.003 agent.py:204(_learn)
               12216921  102.216    0.000 9565.833    0.001 optimizer.py:84(wrapper)
               12216921   53.747    0.000 9103.943    0.001 grad_mode.py:24(decorate_context)
               12216921  348.484    0.000 8936.648    0.001 adam.py:55(step)
              407046869 1541.641    0.000 8881.111    0.000 layers.py:735(check)
               12216921 1848.112    0.000 8173.538    0.001 _functional.py:53(adam)
                4072307  109.341    0.000 7487.245    0.002 agent.py:117(_learn)
                4072307  510.003    0.000 7025.304    0.002 agent.py:212(counterfact)
                4072308  586.811    0.000 6481.207    0.002 layers.py:684(update)
               12216921   58.621    0.000 6337.764    0.001 tensor.py:195(backward)
               12216921   49.220    0.000 6277.524    0.001 __init__.py:68(backward)
               12216921 5989.534    0.000 5989.534    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                9620552  207.784    0.000 5984.564    0.001 agent.py:49(__call__)
                4072307 4811.433    0.001 5977.664    0.001 replaybuffer.py:22(sample_data)
                4072307 4578.561    0.001 5717.329    0.001 replaybuffer.py:67(sample_data)
                4072307 2068.994    0.001 4572.190    0.001 agent.py:88(interveen)
               62960954  139.614    0.000 4303.533    0.000 conv.py:398(forward)
               62960954   81.039    0.000 4096.339    0.000 conv.py:390(_conv_forward)
                4072307 2254.383    0.001 4034.542    0.001 replaybuffer.py:28(teleporter_save_data)
               62960954 4015.299    0.000 4015.299    0.000 {built-in method conv2d}
               49602947 3794.392    0.000 3794.392    0.000 {built-in method tensor}
               57012305 2078.681    0.000 3602.880    0.000 layer.py:151(update)
               40301123   26.000    0.000 3572.575    0.000 game.py:37(board)
               86296817  172.001    0.000 3314.993    0.000 linear.py:93(forward)
              407046869  606.916    0.000 3078.327    0.000 layers.py:729(isFree)
               86296817   71.356    0.000 3048.837    0.000 functional.py:1737(linear)
               86296817 2960.054    0.000 2960.054    0.000 {built-in method torch._C._nn.linear}
                4072307 1877.793    0.000 2868.221    0.001 agent.py:67(modify)
              407046869 1837.676    0.000 2621.449    0.000 layers.py:471(check)
             2709469423 2031.714    0.000 2471.411    0.000 layer.py:95(isFree)
              407046869 1711.007    0.000 2369.005    0.000 layers.py:77(check)
                1498390   29.049    0.000 1952.547    0.001 agent.py:176(choose_action)
               54415929 1878.130    0.000 1878.130    0.000 {built-in method cat}
                4072307   57.341    0.000 1765.571    0.000 agent.py:172(__call__)
              117777294  102.880    0.000 1757.076    0.000 activation.py:713(forward)
               13692859   85.146    0.000 1726.580    0.000 agent.py:59(modify_board)
             6494464572 1171.498    0.000 1682.913    0.000 enum.py:646(__hash__)
                4072307   54.615    0.000 1663.583    0.000 agent.py:112(__call__)
              169414414 1663.474    0.000 1663.474    0.000 {built-in method clone}
              117777294   99.988    0.000 1654.196    0.000 functional.py:1364(leaky_relu)
              228049192 1582.552    0.000 1582.552    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2151970   25.487    0.000 1556.516    0.001 layers.py:740(restart)
              117777294 1534.965    0.000 1534.965    0.000 {built-in method torch._C._nn.leaky_relu}
              228049192 1418.432    0.000 1418.432    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               12216921  244.282    0.000 1404.333    0.000 optimizer.py:189(zero_grad)
              409151138  325.891    0.000 1343.966    0.000 {built-in method builtins.any}
                2151970   12.992    0.000 1313.732    0.001 level.py:8(__init__)
                2151970   87.565    0.000 1190.336    0.001 levels.py:262(generate)
               13692859 1131.596    0.000 1131.596    0.000 {built-in method torch._C._nn.one_hot}
              407046869  799.921    0.000 1048.751    0.000 layers.py:62(check)
               19190034  177.683    0.000 1027.369    0.000 level.py:41(notUsed)
             3240630640  834.737    0.000 1018.075    0.000 layers.py:700(<genexpr>)
                4072307  826.968    0.000 1004.188    0.000 replaybuffer.py:73(CF_save_data)
              114024596  996.176    0.000  996.176    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                4072307   73.358    0.000  873.322    0.000 replaybuffer.py:18(stacker)
             1199060205  859.820    0.000  859.820    0.000 layer.py:146(elements)
                4072307   71.614    0.000  854.400    0.000 replaybuffer.py:63(stacker)
             8773550165  819.865    0.000  819.865    0.000 layer.py:91(positions)
              114024596  794.974    0.000  794.974    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              407230800  163.567    0.000  778.766    0.000 {built-in method builtins.all}
              114024596  757.833    0.000  757.833    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              114024596  744.544    0.000  744.544    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             1647816080  409.205    0.000  664.247    0.000 layers.py:690(<genexpr>)
              798172256  528.336    0.000  653.176    0.000 tensor.py:906(grad)
        8085312283/8085312280  556.740    0.000  629.250    0.000 {built-in method builtins.len}
                4072307  365.433    0.000  618.277    0.000 collector.py:46(collect)
                9620552  224.382    0.000  595.370    0.000 exploration.py:53(softmaxer)
              407046869  379.367    0.000  572.041    0.000 layers.py:48(check)
              114024596  566.141    0.000  566.141    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                8144614  208.904    0.000  562.180    0.000 random.py:315(sample)
             6494510859  511.423    0.000  511.423    0.000 {built-in method builtins.hash}
               12216921   17.104    0.000  508.105    0.000 loss.py:527(forward)
               12216921   45.506    0.000  491.001    0.000 functional.py:2898(mse_loss)
               19190034   17.464    0.000  460.425    0.000 level.py:38(elementsIn)
              407046869  297.946    0.000  431.949    0.000 layers.py:23(check)
              187179580  378.918    0.000  378.918    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              420958041  238.676    0.000  373.752    0.000 layer.py:126(remove)
                1498390  312.694    0.000  353.171    0.000 agent.py:187(convert_values)
             2709469423  306.271    0.000  306.271    0.000 layer.py:203(isBlocking)
              543119474  223.471    0.000  303.935    0.000 layer.py:130(add)
               12216921  302.576    0.000  302.576    0.000 {built-in method torch._C._nn.mse_loss}
                8144616  298.089    0.000  298.089    0.000 {built-in method nonzero}
               19190034  147.716    0.000  293.651    0.000 level.py:39(<listcomp>)
               62960954   45.269    0.000  287.361    0.000 flatten.py:39(forward)
               12218290  276.353    0.000  276.353    0.000 {built-in method max}
              428038332  181.147    0.000  267.512    0.000 random.py:250(_randbelow_with_getrandbits)
               24433842  266.473    0.000  266.473    0.000 {built-in method sum}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579170: <Coconuts_Conver2_1> in cluster <dcc> Done

Job <Coconuts_Conver2_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:07 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Apr 29 10:53:50 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 10:53:50 2021
Terminated at Fri Apr 30 10:49:03 2021
Results reported at Fri Apr 30 10:49:03 2021

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

    CPU time :                                   86047.12 sec.
    Max Memory :                                 3435 MB
    Average Memory :                             3408.95 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12949.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86112 sec.
    Turnaround time :                            288296 sec.

The output (if any) is above this job summary.

