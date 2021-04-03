
# Parameters

    Name :                      causal2_CFagent_convert3-0
    Main :                      CFagent
    Level :                     Levels.Causal2
    Hours :                     13.0
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
    Cf convert :                2
    Minutes used :              775 minutes.
    Hours used :                12 hours.

# Profiling


      28402197534 function calls (28211444943 primitive calls) in 46510.26 seconds

##    Ordered by: cumulative time
   List reduced from 482 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 46510.265 46510.265 {built-in method builtins.exec}
                      1    4.920    4.920 46510.265 46510.265 <string>:1(<module>)
                      1  174.145  174.145 46505.345 46505.345 main.py:96(CFagent)
                6259020   26.404    0.000 15578.248    0.002 agent.py:28(learn)
                6259020  396.945    0.000 12623.150    0.002 learner.py:42(Qlearn)
                2086340   12.199    0.000 7774.638    0.004 game.py:36(step)
                2086340   14.213    0.000 7335.514    0.004 layers.py:594(step)
        213601275/22850375  889.123    0.000 7025.945    0.000 module.py:866(_call_impl)
               16591355   41.325    0.000 6547.155    0.000 network.py:24(forward)
               16591355  215.479    0.000 6394.112    0.000 container.py:117(forward)
                2086340  237.256    0.000 6070.875    0.003 agent.py:53(_learn)
                2086340  233.226    0.000 5535.202    0.003 agent.py:189(_learn)
                6259020   56.473    0.000 4889.525    0.001 optimizer.py:84(wrapper)
                2086340  205.065    0.000 4794.527    0.002 layers.py:18(step)
                2086340 2800.747    0.001 4733.774    0.002 replaybuffer.py:28(teleporter_save_data)
                6259020   29.302    0.000 4643.612    0.001 grad_mode.py:24(decorate_context)
              208495404  271.878    0.000 4567.774    0.000 layer.py:82(move)
                6259020  207.523    0.000 4548.347    0.001 adam.py:55(step)
                2086340  342.932    0.000 4373.528    0.002 agent.py:197(counterfact)
                6259020  964.745    0.000 4127.810    0.001 _functional.py:53(adam)
                2086340 3280.016    0.002 4008.696    0.002 replaybuffer.py:22(sample_data)
                2086340   66.805    0.000 3929.517    0.002 agent.py:114(_learn)
                5165738  151.107    0.000 3394.443    0.001 agent.py:48(__call__)
                2086340 2011.746    0.001 3357.188    0.002 agent.py:85(interveen)
                6259020   27.150    0.000 3348.398    0.001 tensor.py:195(backward)
                2086340 2703.685    0.001 3335.725    0.002 replaybuffer.py:49(sample_data)
                6259020   27.950    0.000 3320.371    0.001 __init__.py:68(backward)
                6259020 3163.892    0.001 3163.892    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              208495404  409.404    0.000 2516.922    0.000 layers.py:611(check)
                2086341  225.948    0.000 2503.231    0.001 layers.py:565(update)
               33182710   74.441    0.000 2378.247    0.000 conv.py:398(forward)
               33182710   44.923    0.000 2265.706    0.000 conv.py:390(_conv_forward)
               33182710 2220.784    0.000 2220.784    0.000 {built-in method conv2d}
               27026467 2135.238    0.000 2135.238    0.000 {built-in method tensor}
               29208767 1205.967    0.000 2131.850    0.000 layer.py:143(NoRock_update)
               21209881   15.321    0.000 1976.157    0.000 game.py:32(board)
               45601385   90.494    0.000 1784.668    0.000 linear.py:93(forward)
              179579004 1721.019    0.000 1721.019    0.000 {built-in method clone}
               45601385   37.202    0.000 1643.768    0.000 functional.py:1737(linear)
               45601385 1597.153    0.000 1597.153    0.000 {built-in method torch._C._nn.linear}
              208292067  296.607    0.000 1487.376    0.000 layers.py:605(isFree)
                2086340  834.102    0.000 1395.328    0.001 agent.py:66(modify)
             1370828757 1022.325    0.000 1190.769    0.000 layer.py:79(isFree)
                 993917   10.351    0.000 1166.053    0.001 agent.py:167(choose_action)
               30201818 1107.343    0.000 1107.343    0.000 {built-in method cat}
                7252078   48.635    0.000  960.806    0.000 agent.py:58(modify_board)
                2086340   41.981    0.000  949.670    0.000 agent.py:163(__call__)
               62192740   50.319    0.000  945.450    0.000 activation.py:713(forward)
                2086340   40.493    0.000  903.829    0.000 agent.py:109(__call__)
               62192740   50.672    0.000  895.131    0.000 functional.py:1364(leaky_relu)
               62192740  834.213    0.000  834.213    0.000 {built-in method torch._C._nn.leaky_relu}
              116835040  803.508    0.000  803.508    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                6259020  130.702    0.000  703.835    0.000 optimizer.py:189(zero_grad)
              116835040  700.857    0.000  700.857    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             2530984651  450.203    0.000  639.376    0.000 enum.py:646(__hash__)
                7252078  636.416    0.000  636.416    0.000 {built-in method torch._C._nn.one_hot}
              208495404  370.194    0.000  588.048    0.000 layers.py:217(check)
              208495404  370.842    0.000  585.285    0.000 layers.py:245(check)
              208634100   61.209    0.000  583.005    0.000 {built-in method builtins.all}
              208495404  363.575    0.000  577.578    0.000 layers.py:231(check)
                2086340   49.705    0.000  561.538    0.000 replaybuffer.py:18(stacker)
              550628304  553.663    0.000  553.663    0.000 layer.py:122(elements)
              655317919  157.830    0.000  546.209    0.000 layers.py:571(<genexpr>)
                1438904   16.581    0.000  525.033    0.000 layers.py:615(restart)
               58417520  474.318    0.000  474.318    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2086340   41.687    0.000  474.281    0.000 replaybuffer.py:45(stacker)
               58417520  420.494    0.000  420.494    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                1438904    9.571    0.000  400.792    0.000 level.py:8(__init__)
               58417520  376.655    0.000  376.655    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               58417520  371.526    0.000  371.526    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              208634100  253.188    0.000  366.165    0.000 layers.py:111(isDone)
              188917422  364.660    0.000  364.660    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                2086340  139.603    0.000  362.395    0.000 replaybuffer.py:55(CF_save_data)
                5165738  127.754    0.000  353.865    0.000 exploration.py:53(softmaxer)
                1438904   19.387    0.000  333.608    0.000 levels.py:151(generate)
             3535280645  329.713    0.000  329.713    0.000 layer.py:75(positions)
              408922724  264.794    0.000  328.601    0.000 tensor.py:906(grad)
                2086340  190.139    0.000  319.535    0.000 collector.py:54(collect)
                4172680  121.748    0.000  317.445    0.000 random.py:315(sample)
              208495404  206.491    0.000  303.632    0.000 layers.py:204(check)
        3899236644/3899236641  261.778    0.000  299.511    0.000 {built-in method builtins.len}
                6905829   62.151    0.000  295.526    0.000 level.py:41(notUsed)
                6259020   10.767    0.000  287.914    0.000 loss.py:527(forward)
                6259020   28.667    0.000  277.147    0.000 functional.py:2898(mse_loss)
               58417520  276.064    0.000  276.064    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                6259021  265.243    0.000  265.243    0.000 {built-in method nonzero}
                3080257   17.674    0.000  249.350    0.000 exploration.py:47(epsilonGreedy)
             2531008650  189.178    0.000  189.178    0.000 {built-in method builtins.hash}
              196642053  120.803    0.000  176.422    0.000 layer.py:102(remove)
                6259020  166.269    0.000  166.269    0.000 {built-in method torch._C._nn.mse_loss}
              246710072  113.479    0.000  161.262    0.000 layer.py:106(add)
               33182710   23.227    0.000  155.291    0.000 flatten.py:39(forward)
                6259843  150.342    0.000  150.342    0.000 {built-in method max}
              215603792   91.380    0.000  136.858    0.000 random.py:250(_randbelow_with_getrandbits)
               12518040  136.231    0.000  136.231    0.000 {built-in method sum}
             1370828757  133.202    0.000  133.202    0.000 layer.py:183(isBlocking)
               33182710  132.065    0.000  132.065    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               29208767  130.669    0.000  130.669    0.000 layer.py:154(<listcomp>)
                1632258   60.111    0.000  129.569    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                8345360   12.324    0.000  127.073    0.000 tensor.py:525(__rsub__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 9493319: <causal2_CFagent_convert3_0> in cluster <dcc> Done

Job <causal2_CFagent_convert3_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Apr  2 22:10:09 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Apr  2 22:22:08 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr  2 22:22:08 2021
Terminated at Sat Apr  3 11:17:22 2021
Results reported at Sat Apr  3 11:17:22 2021

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

    CPU time :                                   46399.07 sec.
    Max Memory :                                 7264 MB
    Average Memory :                             5332.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               9120.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   46516 sec.
    Turnaround time :                            47233 sec.

The output (if any) is above this job summary.

