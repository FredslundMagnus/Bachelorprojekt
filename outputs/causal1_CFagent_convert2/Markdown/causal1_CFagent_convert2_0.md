
# Parameters

    Name :                      causal1_CFagent_convert2-0
    Main :                      CFagent
    Level :                     Levels.Causal1
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
    Cf convert :                1
    Minutes used :              775 minutes.
    Hours used :                12 hours.

# Profiling


      27944245106 function calls (27721493327 primitive calls) in 46519.38 seconds

##    Ordered by: cumulative time
   List reduced from 484 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 46519.384 46519.384 {built-in method builtins.exec}
                      1    4.602    4.602 46519.383 46519.383 <string>:1(<module>)
                      1  170.266  170.266 46514.782 46514.782 main.py:96(CFagent)
                6964584   26.131    0.000 16300.721    0.002 agent.py:28(learn)
                6964574  412.189    0.000 13221.569    0.002 learner.py:42(Qlearn)
        249051012/26300924  946.380    0.000 7723.154    0.000 module.py:866(_call_impl)
               19336350   48.904    0.000 7230.406    0.000 network.py:24(forward)
                2321528   12.266    0.000 7141.485    0.003 game.py:36(step)
               19336350  233.928    0.000 7062.265    0.000 container.py:117(forward)
                2321528   13.505    0.000 6708.274    0.003 layers.py:594(step)
                2321528  249.116    0.000 6340.736    0.003 agent.py:53(_learn)
                2321528  247.006    0.000 5828.376    0.003 agent.py:189(_learn)
                6964574   56.112    0.000 5129.381    0.001 optimizer.py:84(wrapper)
                2321528  550.928    0.000 4966.513    0.002 agent.py:197(counterfact)
                6964574   29.907    0.000 4877.340    0.001 grad_mode.py:24(decorate_context)
                6964574  200.831    0.000 4783.361    0.001 adam.py:55(step)
                2321528 2574.083    0.001 4464.751    0.002 replaybuffer.py:28(teleporter_save_data)
                6964574 1001.863    0.000 4358.683    0.001 _functional.py:53(adam)
                2321528   69.309    0.000 4090.227    0.002 agent.py:114(_learn)
                6185388  162.806    0.000 3789.411    0.001 agent.py:48(__call__)
                2321528  202.095    0.000 3715.838    0.002 layers.py:18(step)
                2321528 2809.575    0.001 3597.818    0.002 replaybuffer.py:22(sample_data)
              231795876  282.406    0.000 3493.170    0.000 layer.py:82(move)
                6964574   27.355    0.000 3491.681    0.001 tensor.py:195(backward)
                6964574   28.746    0.000 3463.396    0.000 __init__.py:68(backward)
                6964574 3305.004    0.000 3305.004    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2321528 1839.244    0.001 3247.166    0.001 agent.py:85(interveen)
                2321528 2358.351    0.001 3050.458    0.001 replaybuffer.py:49(sample_data)
                2321529  240.541    0.000 2956.828    0.001 layers.py:565(update)
               38672700   80.523    0.000 2632.807    0.000 conv.py:398(forward)
               38672700   57.134    0.000 2512.143    0.000 conv.py:390(_conv_forward)
               38672700 2455.009    0.000 2455.009    0.000 {built-in method conv2d}
               30385355 2054.266    0.000 2054.266    0.000 {built-in method tensor}
               53365994  103.540    0.000 1986.180    0.000 linear.py:93(forward)
               27858342 1096.612    0.000 1899.654    0.000 layer.py:143(NoRock_update)
               23639576   15.317    0.000 1881.652    0.000 game.py:32(board)
               53365994   42.496    0.000 1830.238    0.000 functional.py:1737(linear)
               53365994 1777.927    0.000 1777.927    0.000 {built-in method torch._C._nn.linear}
              197451708 1777.279    0.000 1777.279    0.000 {built-in method clone}
                1543342   13.242    0.000 1689.727    0.001 agent.py:167(choose_action)
              231653429  274.793    0.000 1523.512    0.000 layers.py:605(isFree)
                2321528  899.921    0.000 1487.726    0.001 agent.py:66(modify)
              231795876  370.457    0.000 1427.318    0.000 layers.py:611(check)
             1242206152 1071.119    0.000 1248.719    0.000 layer.py:79(isFree)
               34043674 1239.646    0.000 1239.646    0.000 {built-in method cat}
               72702344   55.638    0.000 1058.405    0.000 activation.py:713(forward)
                8506916   49.330    0.000 1049.402    0.000 agent.py:58(modify_board)
                3524012   30.609    0.000 1046.267    0.000 layers.py:615(restart)
               72702344   58.438    0.000 1002.767    0.000 functional.py:1364(leaky_relu)
                2321518   41.568    0.000 1000.925    0.000 agent.py:163(__call__)
                2321528   40.721    0.000  943.775    0.000 agent.py:109(__call__)
               72702344  932.614    0.000  932.614    0.000 {built-in method torch._C._nn.leaky_relu}
              130005368  847.279    0.000  847.279    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                3524012   17.450    0.000  775.797    0.000 level.py:8(__init__)
              130005368  757.721    0.000  757.721    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                6964574  132.153    0.000  744.577    0.000 optimizer.py:189(zero_grad)
                8506916  695.156    0.000  695.156    0.000 {built-in method torch._C._nn.one_hot}
                3524012   41.435    0.000  652.477    0.000 levels.py:122(generate)
                2321528   51.157    0.000  622.923    0.000 replaybuffer.py:18(stacker)
                2321528  281.182    0.000  617.745    0.000 replaybuffer.py:55(CF_save_data)
              232152900   64.347    0.000  608.828    0.000 {built-in method builtins.all}
               13743153  114.712    0.000  575.497    0.000 level.py:41(notUsed)
              719188711  167.264    0.000  570.362    0.000 layers.py:571(<genexpr>)
                2321518   46.372    0.000  532.986    0.000 replaybuffer.py:45(stacker)
               65002684  503.879    0.000  503.879    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              713265327  465.092    0.000  465.092    0.000 layer.py:122(elements)
               65002684  440.553    0.000  440.553    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              231795876  261.259    0.000  404.044    0.000 layers.py:143(check)
             1654095832  279.583    0.000  403.329    0.000 enum.py:646(__hash__)
               65002684  398.088    0.000  398.088    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               65002684  393.529    0.000  393.529    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              232152900  264.348    0.000  381.604    0.000 layers.py:111(isDone)
              208280142  381.595    0.000  381.595    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                6185388  140.774    0.000  380.234    0.000 exploration.py:53(softmaxer)
              455018872  281.490    0.000  349.070    0.000 tensor.py:906(grad)
                2321528  199.786    0.000  338.523    0.000 collector.py:54(collect)
                4643056  118.420    0.000  316.273    0.000 random.py:315(sample)
              231795876  209.213    0.000  305.470    0.000 layers.py:47(check)
        3921386769/3921386766  262.688    0.000  304.103    0.000 {built-in method builtins.len}
               65002684  296.169    0.000  296.169    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              231795876  194.025    0.000  294.929    0.000 layers.py:124(check)
                3864870   19.354    0.000  292.884    0.000 exploration.py:47(epsilonGreedy)
                6964574   12.782    0.000  287.186    0.000 loss.py:527(forward)
                6964574   26.025    0.000  274.404    0.000 functional.py:2898(mse_loss)
                6964585  266.547    0.000  266.547    0.000 {built-in method nonzero}
               21144072   21.494    0.000  232.673    0.000 layer.py:56(restart)
               13743153   10.819    0.000  224.999    0.000 level.py:38(elementsIn)
             2619769286  224.137    0.000  224.137    0.000 layer.py:75(positions)
              329915167  129.976    0.000  183.602    0.000 layer.py:106(add)
              196813708  128.060    0.000  180.322    0.000 layer.py:102(remove)
                3524112   86.460    0.000  173.752    0.000 layers.py:33(reset)
               38672700   25.452    0.000  172.060    0.000 flatten.py:39(forward)
                6964574  169.210    0.000  169.210    0.000 {built-in method torch._C._nn.mse_loss}
              633924052  166.945    0.000  166.945    0.000 level.py:32(inverse)
                6965578  157.999    0.000  157.999    0.000 {built-in method max}
                2089731   70.766    0.000  152.197    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               38672700  146.607    0.000  146.607    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              245963662   97.795    0.000  146.371    0.000 random.py:250(_randbelow_with_getrandbits)
               13929168  145.541    0.000  145.541    0.000 {built-in method sum}
               13743153   70.225    0.000  138.729    0.000 level.py:39(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-5>
Subject: Job 9493315: <causal1_CFagent_convert2_0> in cluster <dcc> Done

Job <causal1_CFagent_convert2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Apr  2 22:10:08 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Apr  2 22:10:09 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr  2 22:10:09 2021
Terminated at Sat Apr  3 11:06:48 2021
Results reported at Sat Apr  3 11:06:48 2021

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

    CPU time :                                   46394.99 sec.
    Max Memory :                                 7603 MB
    Average Memory :                             5441.60 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8781.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   46661 sec.
    Turnaround time :                            46600 sec.

The output (if any) is above this job summary.

